
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1) # Permute the input tensor A
        v2  = torch.bmm(v1, x2)
        return v2

# Initializing the model
m  = Model()
__output__  = m(torch.randn(3,4), torch.randn(3,5))

# Initializing the model without `x2`
m_nop  = Model()
__output_nop__  = m(torch.randn(1, 2, 2), None)

