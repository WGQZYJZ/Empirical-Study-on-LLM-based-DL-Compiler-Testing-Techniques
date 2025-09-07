
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp)
        v2 = v1 + 10.3
        return v2


# Initializing the model
m = Model()
inp = torch.randn(8, 64).float()
x1 = torch.randn(1, 3, 64, 64)

# Generate input tensors for this pattern:
def generate_input_tensors():
    while True:
        yield x1 + inp

for _ in range(10):
    x2 = next(generate_input_tensors())
    