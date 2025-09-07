
class Model(torch.nn.Module):
    def __init__(self, num_ftrs=1024):
        super().__init__()
        self.conv1 = torch.nn.Conv1d(...) # X can be 1, 3, or 4 representing the dimension
        self.relu   = torch.nn.ReLU()
        self.conv2 = torch.nn.Conv1d(...) 
        ...
        for i in range(n_layers-1):
            if i % n_groups == 0:
                bn = BatchNorm1d(...) # X should match with ConvXd
            else: 
                bn = BatchNorm1d(...)

            self.add_module('layer%d' % (i+1), Layer1d(...))
        self.conv = torch.nn.ConvNd(...)

    def forward(self, x):
        v1 = self.relu(self.conv1(x))  # Fuse conv and relu into a single convolution layer with X channels each
        if not self._training: 
            bn = BatchNorm1d(...)
            bn(v1)  # Remove batch normalization from the graph

        for i in range(n_layers-2):
            v2 = self.layer%d(...)(v1)    # Pass through a layer
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 1024)
