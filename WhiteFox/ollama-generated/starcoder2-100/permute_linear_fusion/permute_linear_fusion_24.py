class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        # permute the input 3D tensor to 2D tensor in a single call.
        v0 = torch.permute(x1, (0, 2, 1))
        print(v0)

        # apply a linear layer on top of the permuted data and use the output for another linear operation.
        return torch.nn.functional.linear(
            v0,
            torch.nn.Linear(
                in_features=torch.Size((3,))
            ).weight,  # weight matrix is [2x1], that is, a 2D matrix with only one column
            bias=None).matmul(
             torch.nn.Linear(
                 out_features=torch.Size((1, )) 
             ).weight).add_(
             torch.nn.Linear(out_features=3) 
             .bias).squeeze()


