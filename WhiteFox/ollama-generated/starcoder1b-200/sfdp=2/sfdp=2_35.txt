
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
        self.dropout = torch.nn.functional.dropout
    
    def forward(self, x):
        q = self.conv1(x)
        k = self.conv2(x)
        qk = torch.matmul(q, k.transpose(-2, -1))
        qk_scale_factor = torch.rsqrt(torch.mean(qk ** 2, dim=-1).clamp_(min=1e-6))
        qk = qk * qk_scale_factor
        softmax_qk = qk.softmax(dim=-1)
        output = self.dropout(softmax_qk)
        return output


# Initializing the model
m = Model()


