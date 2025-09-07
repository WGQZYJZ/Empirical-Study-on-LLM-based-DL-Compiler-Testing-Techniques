
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v = torch.nn.Linear()(x1) + 4.735908 * torch.nn.Tanh()(x2)

# Initializing the model