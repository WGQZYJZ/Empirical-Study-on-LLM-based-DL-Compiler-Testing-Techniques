
class Model(torch.nn.Module):
    def __init__(self, num_classes=None, activation=F.relu, drop_rate=0.5):
        super().__init__()
 
        self.num_classes = num_classes
 
        self.cnn1 = torch.nn.Conv2d(3, 8, 4, stride=2, padding=1)
        self.cnn2 = torch.nn.Conv2d(8, 8, 5, stride=2, padding=0)
 
        # If the given num_classes is not provided, we do not need any extra linear layers
        if num_classes is not None:
            self.linear = nn.Linear(12 * 2 * 2, num_classes)
 
    def forward(self, x):
        # TODO: Implement this line and generate the input tensor for the newly generated model. The output of the cnn should be an image that has the shape of (5, 8, 4, 4) where the width of each column is 5 and the height of each row is 8
        x = self.cnn1(x) + 0.5
        x = self.cnn2(x) + 0.70710678118654756
 
        # TODO: Implement this line for generating the input tensor for the newly generated model
        # This is a split operation and two cat operations should be used, which split along (1), (3, 2) and concatenate along (1, 3, 2).
        x = torch.split(x, [4, 5], dim=1) + 0.5
        x = torch.cat([torch.split(i, [2]) for i in x], dim=1)
 
        # TODO: Implement this line and generate the output of the newly generated model by using the input tensor you have created in step 3 and then applying the activation function to it.
        x = self.linear(x)
        return x


# Initializing the model
m = Model()


