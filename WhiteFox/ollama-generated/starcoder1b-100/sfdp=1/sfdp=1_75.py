
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        vq = torch.matmul(x1, x1)
        vk = torch.randn(1, 8)
        vk.requires_grad_()
        scaled_qk = vq / vk.sqrt()
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(x1)
        return output


# Initializing the model
m = Model()


