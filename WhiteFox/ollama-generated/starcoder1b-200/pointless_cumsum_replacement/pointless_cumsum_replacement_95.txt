
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input_tensor = torch.randn(3, 64, 64)
 
    def forward(self, arg1, arg2):
        return torch.full([arg1, arg2], 1, dtype=torch.float, layout=torch.strided, device=torch.device('cpu'), pin_memory=False)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
