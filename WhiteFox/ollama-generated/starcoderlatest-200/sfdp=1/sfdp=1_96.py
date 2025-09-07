
class AttentionModel(torch.nn.Module):
    def __init__(self, key_dim, query_dim):
        super().__init__()
        self.key_dim = key_dim
        self.query_dim = query_dim
 
        # TODO: define the layer that performs a pointwise convolution with kernel size 1 and stride 1
        # Hint: please see the Conv2d layer of torch.nn module
 
        # TODO: define the fully connected layers that use ReLU as nonlinearity, where one fully-connected layer applies to both the query and key tensors
        self.query = None 
        self.key = None
 
    def forward(self, x1):
        