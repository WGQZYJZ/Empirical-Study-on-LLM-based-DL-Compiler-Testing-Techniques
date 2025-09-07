
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        # First convolutional layer: We only compute the output of the first half of the tensor
        x0 = x1[:, :, :, :int(x1.shape[3] * .5)].contiguous()
 
        # Second convolutional layer: We now have a 2x2 tensor which is equivalent to `1 + k_t` for some `k_t`.
        # Therefore, we need the output of this convolution to be multiplied by the value, and then the output is added to a bias vector.
        # We multiply the first half of the x0 tensor with the query (i.e., v), then we add the bias and then softmax it.
        v1 = self.conv2(x0).contiguous() * self.query  + self.bias
        output = torch.nn.functional.softmax(v1, dim=-1)
 
        # Now that we have a batch-first representation of our input tensor with shape (batch_size, 3, height, width),
        # we can now apply the first half of the second convolutional layer to it.
        x1 = x1[:, :, int(x1.shape[2] * .5):].contiguous() * output
 
        # Finally, we compute the result for the input by applying a 3-D convolution on top of the output.
        x0 = torch.cat([x1, x0], dim=-1)
        return self.conv1(x0)

# Inputs to the model
query = torch.randn(2, 8, 64, 64)
value  = torch.randn(2, 8, 64, 64)
bias   = torch.zeros(2).float().to('cuda')
scale_factor = torch.ones(2).float().to('cuda')
dropout_p = .1
m = Model()
x0  = m(query)
