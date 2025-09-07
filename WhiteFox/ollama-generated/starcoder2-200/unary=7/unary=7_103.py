
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64 * 64, 32 * 32)

    def forward(self, x):
        v0 = self.linear1(x).view(-1, 32, 32, 3) # View the output of linear transformation with size -1 to have three dimensions

        return v0

m = Model()

inputs_to_model = torch.randn(48 * 48, 64 * 64)
__output__  = m(inputs_to_model)