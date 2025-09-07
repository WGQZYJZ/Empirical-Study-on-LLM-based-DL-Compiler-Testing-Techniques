
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.tensor(20)
        self.softmax  = torch.nn.Softmax(-1)
        self.dropout  = torch.nn.Dropout(p=0.3, inplace=True)

    def forward(self, query: torch.Tensor): # [2, 5]
        keys  = torch.rand((2, 7)) # [2, 7]
        values  = torch.rand((1, 7), (2, 6)) # [(2, 7),(1, 7)]
        inv_scale = self.scale / keys.norm(dim=-1).max() 
        v1 = query @ keys.transpose(-2,-1) * inv_scale # [2,5] @ [2,7]*[7, 6] = [2, 5]
        v2 = self.softmax(v1) # Apply softmax to the scaled dot product of the query and the key
        v3 = torch.nn.functional.dropout(v2, p=0.3, inplace=True) #[2, 5]
        return v3 @ values # [2 ,6] * [7 , 1] = [(2 , 5),(2 , 5)]


__input__ = torch.randn((2, 4))

# Inputs to the model
x2  = torch.randn(8)