
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t0 = torch.split(x1, (64, 32), dim=0)  # Split the input tensor along dimension 0
        t1 = t0[0] * 0.5  # Multiply output of first split operation by 0.5
        t2 = t0[1] * 0.7071067811865476  # Multiply output of second split operation by 0.7071067811865476
        t3 = torch.erf(t2)  # Apply error function to the second split operation
        t4 = t3 + 1  # Add 1 to the output of the second split operation
        return t4


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
