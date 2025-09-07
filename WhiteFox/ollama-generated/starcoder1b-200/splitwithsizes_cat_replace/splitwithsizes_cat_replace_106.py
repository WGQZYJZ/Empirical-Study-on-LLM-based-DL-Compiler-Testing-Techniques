
class Model(torch.nn.Module):
    def __init__(self, dim_x: int = 1024):
        super().__init__()

        self.conv_x = torch.nn.Conv2d(dim_x, 8, kernel_size=1, stride=1, padding=1)
        self.split_x = torch.nn.utils.rnn.SplitTensor(torch.nn.Sequential(), dim=0)
        self.cat_x = torch.nn.utils.rnn.CatTensor()

        self.conv_y = torch.nn.Conv2d(8, 16, kernel_size=1, stride=1, padding=1)
        self.split_y = torch.nn.utils.rnn.SplitTensor(torch.nn.Sequential(), dim=0)
        self.cat_y = torch.nn.utils.rnn.CatTensor()

    def forward(self, x1: torch.Tensor, y1: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        # Apply a linear transformation to the input
        x2  = x1.view((x1.shape[0], -1))
        v1  = self.conv_x(x2)
        v2  = v1  * 0.5
        v3  = v1  * 0.7071067811865476
        v4  = torch.erf(v3)
        v5  = v4  + 1
        v6  = self.cat_x(self.split_x((v2, v3)))  # Split the input into two tensors according to `dim=0`

        v7  = v6  * y1  # Multiply each tensor in the result of the split operation by each element in the corresponding output vector in `y1`.
        return (self.cat_y((v7)),
                self.cat_y((v4)))

# Initializing the model
m = Model()


