
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2):
       t3 = torch.cat([t1, t2], dim=...)
       t4 = t3.view(t3.size()[-1] + 4)
       t5 = torch.relu(t4)

# Initializing the model with initial tensors as inputs to the model
m = Model()

x1 = torch.randn(2, 3) # Shape (B, 3) where B is batch size
x2 = torch.randn(2, 50) # Shape (B, 50) where B is batch size
x_inputs = {
    't1': x1,
    't2': x2
}


