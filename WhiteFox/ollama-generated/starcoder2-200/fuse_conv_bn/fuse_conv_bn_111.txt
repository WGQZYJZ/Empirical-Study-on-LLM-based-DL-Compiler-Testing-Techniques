
class ConvBN(torch.nn.Module):
    def __init__(self, conv: torch.nn.ConvNd) -> None:
        super().__init__()
        self._conv = conv

    def forward(self, x1):
        v3  = torch.nn.functional.batch_norm(
            torch.nn.functional.convNd(x1, weight=self._conv.weight),
            self._conv.bias)
        return v3

# Initializing the model: batch normalization, conv, and ConvBN
batchNorm = torch.nn.BatchNorm2d(8)
conv  = torch.nn.ConvXd([9], [16]) # X can be 1, 2, or 3 representing the dimension
model = ConvBN(conv)


# Input to the model: an input tensor with shape (10, 9, 4), with batch size of 8. 
# Input_tensor is a view from output Tensor 10x30x5x4
input_tensor  = torch.randn(2 * conv._kernel_size[0] + 1,
                            input_tensor.shape[-1],
                            input_tensor.shape[-1])

input_tensor = torch.nn.functional.convNd(input_tensor, weight=conv.weight)


# Output of the model: an output tensor with shape (15034, 9). 
__output__  = torch.nn.functional.batchNorm(
            torch.nn.functional.convNd(input_tensor,
                                       weight=conv.weight), 
            batchNorm._weights)

print(__output__.size())

