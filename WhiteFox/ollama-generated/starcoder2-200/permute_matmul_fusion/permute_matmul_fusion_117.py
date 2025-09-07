
class Model(torch.nn.Module):
    def __init__(self, input1_dim=2, input2_dim=3):
        super().__init__()
        self.linear = torch.nn.Linear(input1_dim, 3)

    def forward(self, x1, x2):
      v1 = x1.permute(0, 2, 1)
      v2 = x2.permute(0, 2, 1)

      v3 = torch.bmm(v1, v2)
      
      return self.linear(v3)


# Initializing the model