
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, inp1, inp2):
        
        out = torch.mm(inp1, inp2) + inp  # Please generate a valid PyTorch model example with public PyTorch APIs meets the specified requirements. Plus, please also generate the input tensor for the newly generated model. The model should be different from the previous one.
        return out


m  = Model()

x1 = torch.randn(5)
x2 = torch.randn(784) # Initializing the model

x3 = torch.randn(5, 6)
