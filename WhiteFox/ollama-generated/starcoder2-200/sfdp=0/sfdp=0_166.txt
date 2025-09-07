

import torch 
import torch.nn as nn 

class ScaledDotProductAttention(nn.Module):
    def __init__(self, dmodel=512):
        super().__init__()
        self.dmodel = dmodel
        self.scale = np.sqrt(torch.Tensor([float(dmodel)])).item()
    
    def forward(self, Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor) -> Tuple[torch.Tensor]:
        
        query_dim  = Q.size(-1)
        
        key   = self._scaled_dot_product(Q,K,torch.ones([query_dim]))
        value     = V
        attention_weights       = key.softmax(dim=-1)
        output              = torch.matmul(attention_weights,value)
        
        
        return output, attention_weights
        
    def _scaled_dot_product(self, Q: torch.Tensor, K: torch.Tensor, 
                           scale: float = None):
        
        # Compute scaled dot product
        
        dim1 = len(Q.size())-2
        dim2 = int(len(K.size()))-dim1
        
        query = Q.permute((0,*[i+1 for i in range (dim1)],*[j 
                                                        for j in range(dim1,dim2)]))
        
        key_transpose   = K.permute(*[0]*int(len(Q.size()) - dim2),
                                      *[i-dim1 for i in range(query_dim+dim1) ],
                                      *list(range(key_transpose)))
        
            
        scaled_dot_product  = torch.matmul(query, key_transpose)/(scale or self.scale)**0.5
        
        return scaled_dot_product


# Initializing the model
m  = ScaledDotProductAttention()

Q   = torch.randn(1,3,4)
K   = torch.randn(1,8,7)
V   = torch.randn(1,8,6)
__output__,__output2__    = m(Q, K, V)

