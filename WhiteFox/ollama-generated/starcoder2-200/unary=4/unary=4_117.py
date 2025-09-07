
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 * 0.5
        v3  = v1 * 0.7071067811865476
        v4  = torch.erf(v3)
        v5  = v4 + 1
        v6  = v2 * v5
        return v6


# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 8)

 # Input tensor for the newly generated model with shape [B, N] where B is batch size and N is input_tensor size. For example if B=32, C=4096 and H=56, W=76 then input should be of shape [32, 4096*56*76]. Note that this input shape matches the original model (for simplicity)
x1 = torch.randn(32, 8)
__output__  = m(x1)

