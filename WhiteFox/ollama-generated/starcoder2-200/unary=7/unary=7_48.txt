
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
 
    def forward(self, x2):
        v7 = self.linear1(x2)
        clamped_output = (v7).clamp_(0.,6.)
        output_with_offset  = clamped_output + 3
        scaled_output = output_with_offset / 6 
        return scaled_output


# Initializing the model
n = Model()

# Inputs to the model
x2  = torch.randn(1, 3)

__output__  = n(x2)
