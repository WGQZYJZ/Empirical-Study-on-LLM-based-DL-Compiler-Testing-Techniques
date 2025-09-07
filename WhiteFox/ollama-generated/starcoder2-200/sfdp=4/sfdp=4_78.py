import torch

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(512, 8)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, mask_token: torch.Tensor) -> torch.Tensor:
        
        v_mask  = torch.where(torch.sum(key, dim=0)!=torch.zeros((128,)),mask_token,torch.ones(512))
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) 
        qk  = qk+v_mask
        
        attn_weight = torch.softmax(qk,dim=-1)
    
        return attn_weight @ value

# Initializing the model and its weights
m  = Model()
torch.nn.init.xavier_uniform_(m.attn.weight) # Initialize the weight of the linear layer


# Inputs to the model
query = torch.randn(1,320,) # Shape: (batch_size, num_heads * head_dim), the size of a single head of transformer-encoder
key = <KEY>) # Shape: same as query except batch and seq length dimensions are swapped.
value = torch.randn(512,) # shape is: (num heads x batch size, sequence length, head dim)
mask_token  = torch.ones((320,1))


# Calling the forward pass of model
