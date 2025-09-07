
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 6, 5) # Convolutional layer with 5x5 kernel
        self.bn1 = torch.nn.BatchNorm2d(num_features=6, track_running_stats=True) 
        # Batch normalization with tracking statistics

    def forward(self, x):

        # Model input
        v1 = torch.randn([30, 3, 28, 28])
        
        v4 = torch.nn.functional.conv2d(x1, self.conv1.weight)
        v5 = torch.nn.functional.batch_norm(v4) # Batch normalization using convolutional output and track statistics
        return v5

# Initializing the model
model  = Model()


# Inputs to the model
input1  = torch.randn([30, 3, 28, 28])

# Expected model output:
output_expected__ = model(input1)

# Actual model output using torch.nn module
output_actual__ = model(v1)

# The results should match exactly since the model inputs are not modified in this case

