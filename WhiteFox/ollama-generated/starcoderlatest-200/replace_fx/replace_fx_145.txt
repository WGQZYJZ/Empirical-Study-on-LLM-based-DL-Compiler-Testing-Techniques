 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, ...) # Replace with `lowmem_dropout`
        ... 
        return output
        
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2000, 5)
