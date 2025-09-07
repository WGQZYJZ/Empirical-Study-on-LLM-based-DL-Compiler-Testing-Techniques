
import torch 

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 0.1
        
    def forward(self, q, k, v):
        scaled_dot_product  = torch.matmul(q, k.transpose(-2, -1)) / torch.sqrt(torch.tensor(k).shape[-1])
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(v)
        return output

m  = Model()

