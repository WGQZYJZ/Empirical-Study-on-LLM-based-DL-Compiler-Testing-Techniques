
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.qk = torch.nn.Linear(4, 3)
 
    def forward(self, x1):
        v0 = self.qk(x1)
        return v0


# Initializing the model
m  = Model()

# Inputs to the model
x2 = torch.randn(56789, 4).cuda() # This is to get the correct size of the model output
 
# Initial values for the weights and bias used in `qk`
m0_qk_weight  = torch.tensor([[-1., -3., -5.], [2., 4., 6.]])
m0_qk_bias    = torch.tensor([-7., 9., 11.])
 
# Model output for the input `x2` with model weight and bias intializations set to `m0_qk_weight`, `m0_qk_bias`.
