
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight)
        v2 = v1.permute(0, 2, 1)
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
    x1 = torch.randn(3, 4, 5)

    print(x1)

     [[[ 1.8796   -0.7804    0.4935   0.2559]
      [-0.0703   -0.1177   -0.2996    0.1035]]

      [[-0.8286   -0.2855   -0.0504   -0.7248]
      [-0.3663    0.463     0.0675   -0.598 ]]

      [[ 1.374    -0.2523   -0.6531   -0.7607]
      [ 0.5457    0.4514    0.7603   -0.4598]]]

