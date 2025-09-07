
class Model(torch.nn.Module):
    def __init__(self, num_layers):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1).contiguous()
        # [batch, channels, height, width] => [batch, width, height, channels]
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)

        # Reshape the tensor after performing pointwise linear operation.
        t3 = torch.relu(t2.view(-1, 1))
        return t3

