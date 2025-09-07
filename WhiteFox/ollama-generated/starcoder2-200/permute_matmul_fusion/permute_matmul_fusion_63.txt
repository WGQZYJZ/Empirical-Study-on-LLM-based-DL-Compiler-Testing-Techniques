
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.tensor([[4., 5.], [7., -3.]], device=x1.device)

        v1_permuted = x1.permute(0, 2, 1).to(v1.device)
        v2_permuted = x2.permute(0, 2, 1).to(v1.device)
        v3 = torch.bmm(v1_permuted, v2_permuted)

        v4 = torch.tensor([[-8., -5.], [-7., 9.]], device=x1.device)
        v4_permuted = x1.permute(0, 2, 1).to(v1.device)
        v3 += torch.bmm(v4_permuted, v1)

        v5 = torch.tensor([[-9., -7.], [-8., 6.]], device=x1.device)
        v5_permuted = x2.permute(0, 2, 1).to(v1.device)
        v3 += torch.bmm(v5_permuted, v4)

        v6 = torch.tensor([[-9., -7.], [-8., 6.]], device=x1.device)
        v7 = x1 * v2 + torch.zeros(0).to(v1.device)
        v3 += torch.bmm(v5_permuted, v4 + v6)

        v3 += x2.to(v1.device)
        return v3

# Initializing the model
m = Model()

