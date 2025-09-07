
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 * 64, 8)

    def forward(self, x1, x2):
        v1 = self.linear(torch.cat((x1.view(-1), x2.view(-1)), dim=0))
        v2 = v1 - torch.randn_like(v1)
        v3 = F.relu(v2)
        return v3


# Initializing the model
m = Model2()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64).to('cuda:0') # Replace cuda:0 with GPU device index you want
