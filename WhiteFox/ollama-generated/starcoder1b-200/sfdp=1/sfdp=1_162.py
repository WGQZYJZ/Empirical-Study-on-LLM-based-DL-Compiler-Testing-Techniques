
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(d_model, d_model)
        self.scale = nn.Parameter(torch.ones(1))
 
    def forward(self, x1, x2):
        k, v = self.qkv(x1), self.qkv(x2)
        dk = torch.matmul(k, inv_scale_factor).softmax(-1)  # Compute dropout output
        return output


# Initializing the model
m = Model()


# Inputs to the model
inputs = (torch.randn(4, 32, 608, 608), torch.randn(4, 32, 608, 608))
