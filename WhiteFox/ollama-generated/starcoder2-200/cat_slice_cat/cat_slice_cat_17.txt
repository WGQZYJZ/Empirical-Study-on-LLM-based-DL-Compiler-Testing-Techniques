
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.cat(x1)[:, 0:9223372036854775807] # [1:size]
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = [(torch.randn(3, 224, 224), torch.randn(3, 226, 226))] * 5 # [1:size]
