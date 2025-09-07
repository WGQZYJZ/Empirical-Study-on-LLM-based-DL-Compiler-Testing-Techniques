
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0 = torch.rand_like(x1).add_(2)
        v1 = torch.nn.functional.dropout(v0, 0.5)

        v3 = torch.nn.functional.linear(
            v1,
            torch.zeros([4, 6], device="cuda"),
            torch.full((6,), fill_value=4.)
        )
        v4 = torch.nn.functional.relu(v3) # Relu for backward-compatibility
        return v4


m = Model()
x1 = torch.rand(2, 5).to("cuda")
