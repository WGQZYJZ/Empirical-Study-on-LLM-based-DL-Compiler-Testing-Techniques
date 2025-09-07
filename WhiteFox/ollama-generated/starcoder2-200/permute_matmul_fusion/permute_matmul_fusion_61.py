
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1  = torch.nn.Linear(2, 4)

    def forward(self, x1):
        v1 = x1.permute(0, 3, 2, 1).contiguous()  # contiguous to avoid memory conflict in the bmm operation.
        v2 = self.linear1(v1)
        v3 = torch.bmm(input_tensor_A, input_tensor_B, alpha=0.75, beta=0.48)
        return v2


# Initializing the model