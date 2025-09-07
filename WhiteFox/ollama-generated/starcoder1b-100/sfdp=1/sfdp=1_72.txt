
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        # Input shape: (batch_size, channels, length, width)
        # Note that the channels dimension corresponds to the batch dimension of the input tensor, as in pytorch.

        # Apply the pointwise convolution with kernel size 1 over the input.
        # Note that we perform a 2D convolution on each channel separately.
        x1 = self.conv(x1)
        # Scale the input by an inverse scale factor to make the dot product more computable.
        x2 = x1.mul_(-0.5).add_(1)
        # Apply the attention function with queries = x, keys = x and values = x2.
        # Note that we only need to multiply the output of the attention function by the value tensor.
        kq = torch.matmul(x1, x2)  # Compute the dot product of the query and key tensors
        kq = kq / math.sqrt(float(key_dim))  # Normalize the dot product so that it is computable for the next step
        # Apply dropout to apply a mask to the softmax output to avoid overfitting.
        x = torch.nn.functional.dropout(x, p=self.dropout_p)
        # The final step is to compute the dot product of the output from the attention function and the value tensor.
        return torch.matmul(x, kq)


# Initializing the model
m  = Model()

