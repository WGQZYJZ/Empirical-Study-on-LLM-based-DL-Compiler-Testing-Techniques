
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3072) # Input 1: query matrix with 2 samples and 3072 dimensions each
k = torch.randn(3072, 4960) # Key tensor with 3072 dimensions and 4960 components per sample in each row. Each of these components will be used to compute the dot product with a value matrix of 4960 columns.
v = torch.randn(4960, 1008) # Value tensor with 4960 dimensions and 1008 components per sample in each row. Each component will be used as a factor in computing the dot product with another tensor of size 3072 by 1008.
m = Model()

