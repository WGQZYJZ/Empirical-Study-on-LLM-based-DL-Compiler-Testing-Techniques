
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        split = torch.split(x1, 2048)
        cat = torch.cat([split[i] for i in range(len(split))], dim=3) # <|>
        return cat

# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(1, 64 * 80 * 256 + 397, dtype=torch.float32, device="cpu")


