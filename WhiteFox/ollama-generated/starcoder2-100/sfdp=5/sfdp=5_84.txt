
import torch
from torch import nn, einsum

def to_2d(tensor):
    return tensor.reshape(-1, 64)

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.query = nn.Linear(784, 500)
        self.key = nn.Linear(784, 500)
        self.attn_mask = torch.full((1, 128), -float('inf'), device='cuda')

    def forward(self, input):

        # compute the query and key
        q = self.query(input).reshape(-1, 32, 64)
        k = self.key(input).reshape(-1, 32, 64)
        
        # compute dot product of q with k and scale it by sqrt of dim size
        attn_weight = einsum("ijl,ijk->ijl", (q / torch.sqrt(torch.tensor(500)), k))
        # add attn mask to scaled dot weight, scale dot weight and dropout
        attn_weight += self.attn_mask.expand(*attn_weight.shape)  # scale dot weight: scale dot weight by a constant attn maks
        attn_weight = torch.softmax(attn_weight, -1).float()
        attn_weight /= attn_weight.sum(-2).unsqueeze(-1) # compute the dropout mask, then apply it to attn weigth
        attn_weight = torch.dropout(attn_weight, 0.5)
        
        # compute dot product of query with value (plus softmax of scaled dot product, drop out, multiplying result with query)
        output1 = einsum("ijl,jl->il", (attn_weight, q))
        return output1


# Input to the model for testing
input  = torch.randn(32768).reshape((4096, 1, 32)).cuda()

# Initializing the model
model = Model().cuda()

# Input to the model for testing with dropout
model.eval()

