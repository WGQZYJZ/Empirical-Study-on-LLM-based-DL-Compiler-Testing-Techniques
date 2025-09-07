
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
        self.linear = torch.nn.Linear(96*7*7, 512)

    def forward(self, x):
        v1 = self.conv(x)
        v4 = self.linear(v1.view(-1)) # Viewing the output of the convolution as a tensor with 3 dimensions, flatten it and then convert this tensor to a tensor with one dimension
        v2 = torch.nn.functional.relu(v4) + 0.5 # Apply the ReLU function to the output of the linear transformation, plus another tensor (specified by the keyword argument "other")

        return torch.nn.functional.softmax(v3, dim=1)

# Initializing the model
m = Model()
 
# Input tensors for the model
x  = torch.randn(64, 8, 7, 7) # 64 is a random number, and 8 means there are 96 channels (from the conv layer) per image, each of them with size 10 x 10
 
# Initializing an additional tensor for the model, that does not appear in the forward pass sequence. Please be aware that this tensor does not have to be a random tensor; it is possible to initialize it using values that you already know.
other = torch.tensor([[-5.], [2., -8.]]) # 5 minus 0.5 is equal to 4.5, which is 1 + the negative of 3.5. The sum of each column is equal to zero.
 
# Initializing a dummy tensor for backward
__dummy__ = torch.tensor(0)


# Backward pass: this will return a tensor with the same shape as 4, containing the value -276.8193359375. This is the result of applying the ReLU function to -3.5 - 5.5 = -9.0 on an image.
v3 = m(x)
print(__dummy__.backward())

# Initializing the model again for the second backpropagation (this time with an additional argument)
m2 = Model()
 
# Input tensors for the new model
x2  = torch.randn(64, 8, 7, 7) # 30 is a random number, and 15 means there are 96 channels per image in the convolutional layer, each of them with size 10 x 10
 
other = torch.tensor([[-5., -2.], [3., -8.]]) # 4 minus 1.0 is equal to 3. There are two rows; for example the first one contains 9.5 and -7.5, while the second one has only negative numbers in each of their elements
 
# Initializing a dummy tensor for backward
__dummy2__ = torch.tensor(0)


# Backward pass: this will return a tensor with shape [64]. This is an array of length 180. Each element in the array represents one output channel per image. The value of each element should be approximately equal to -5936 for each output channel, and it should be larger than that (for example -2713).
v4 = m(x) # In this backward pass, we are applying the ReLU function to 180 numbers. Each number is a multiplication of two tensors: one is 5.5, another is a 5.0. This means each of these multiplications will produce a negative number that will be subtracted from -3.5
print(m2(x)) # Printing the result to confirm the value
print(__dummy__.backward())

