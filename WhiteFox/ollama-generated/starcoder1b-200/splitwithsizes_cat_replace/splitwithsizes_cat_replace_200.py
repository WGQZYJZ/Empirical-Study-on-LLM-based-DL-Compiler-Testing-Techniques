
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y2):
        if 42:
            torch.split(...) # split_sizes=[42]

        elif 5:
            torch.cat(...) # concatenate_dim=5


# Inputs to the model
x1 = ... # Input of shape [batch_size, feature_size1, feature_size2, ...], where feature_size is the length of `split_sizes`
y2 = ... # Input of shape [feature_size1, feature_size2, ...]
