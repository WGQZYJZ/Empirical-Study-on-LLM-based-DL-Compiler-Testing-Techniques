
class ConvModel(torch.nn.Module):
    def __init__(self, conv_size):
        super().__init__()

        # Construct the model
        self._input = torch.randn(100, 32, conv_size - 1)
        self._conv1d = torch.nn.Conv1d(in_channels=48, out_channels=64, kernel_size=7)
        self._batchnorm = torch.nn.BatchNorm1d(num_features=64)

    def forward(self):

        # Run the model with batch normalization enabled. The 2nd parameter is set to True as it represents
        # batch norm in evaluation mode
        convOutput = self._conv1d(self._input)
        
        # Fuse the convolutional layer and batch normalization layer into a single layer, and run the batch normalization
        # layer without tracking running stats for the input. This optimization will be enabled only when the batch 
        # normalization layer is tracking running statistics (in eval mode).
        conv_bnOutput = self._batchnorm(convOutput)

        return conv_bnOutput

model = ConvModel(150)

