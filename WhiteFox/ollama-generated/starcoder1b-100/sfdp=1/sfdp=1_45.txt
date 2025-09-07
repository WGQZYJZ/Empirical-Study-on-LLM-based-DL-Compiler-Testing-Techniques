
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1)

    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1))  # Compute the dot product of each pair of input tensors
        scale_factor = torch.rsqrt(torch.mean(qk.pow(2).sum(-1), dim=-1, keepdim=True) + eps)  # Compute the inverse scaling factor by applying sqrt over all axes
        dropout_qk = torch.nn.functional.dropout(qk.div(scale_factor), p=dropout_p)  # Apply dropout to the softmax output
        v  = self.conv1(dropout_qk)  # Convolve each pair of input tensors with a single convolutional layer
        w  = self.conv2(v)  # Convolve each pair of input tensors with a second convolutional layer
        return w


# Initializing the model
m  = Model()


