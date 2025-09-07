
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2) 
        v2  = [v1] * 3 # Repeats the result of matrix multiplication three times in a list
        v3  = torch.cat(v2, dim=0)  # Concatenate along dimension zero (default)
        return v3


# Initializing the model
m  = Model() 

# Input tensors for model initialization 
x1 = torch.randn(4, 64, 64, 3).long()
x2 = torch.randn(750, 8, 9) # input tensor shape (4, 750, 8, 9)
__output__   = m(x1, x2)

