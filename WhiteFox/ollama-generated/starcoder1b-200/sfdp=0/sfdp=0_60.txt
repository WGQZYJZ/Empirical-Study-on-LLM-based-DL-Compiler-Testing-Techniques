
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.scale = torch.nn.Parameter(torch.tensor(1.0), requires_grad=True)
 
    def forward(self, x1):
        query  = self.conv(x1).contiguous().view(-1, 3, 64, 64)  # [N, C, H, W]
        key     = x1.contiguous().view(-1, 3, 1, 1)          # [N, C, 1, 1]
        inv_scale = torch.sqrt(torch.Tensor([float(self.conv.kernel_size[0]) * float(self.conv.kernel_size[0])] * query.shape[1]))
        attention_weights = query.mm(key.transpose(-2, -1)) / (inv_scale ** 0.5)  # [N, C]
        output = attention_weights.matmul(x1)

        return output


# Initializing the model
m = Model()

