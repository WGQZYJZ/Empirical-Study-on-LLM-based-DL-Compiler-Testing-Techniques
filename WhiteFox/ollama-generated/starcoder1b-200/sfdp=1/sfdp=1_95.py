
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        qk = torch.matmul(v1, v1.transpose(-2, -1))
        scale_factor = torch.sqrt(torch.diagonal(qk).reshape((v1.shape[0], 1)))  # Compute the inverse square root of the dot product of two tensors
        softmax_qk = qk / scale_factor  # Apply the softmax function to the scaled dot product
        output = dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return output


# Initializing the model
m = Model()


