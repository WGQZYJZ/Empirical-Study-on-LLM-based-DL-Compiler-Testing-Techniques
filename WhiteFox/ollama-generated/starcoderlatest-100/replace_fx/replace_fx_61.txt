
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        # Dropout with replacement of torch.nn.functional.dropout and lowmem dropout (see the above description).
        x2 = torch.nn.functional.dropout(x1, p=0.2)

        # Random Tensor with replacement of torch.rand_like and random_() function. 
        x3 = torch.rand_like(x1, dtype=torch.int64)
        
        return x1, x2, x3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 5, 7)
