
class Model(torch.nn.Module):
    def __init__(self, num_classes=1000):
        super().__init__()
        self.backbone = torch.hub.load('pytorch/vision:v0.9.0', 'resnet18', pretrained=True)
        self.classification = torch.nn.Linear(in_features=512, out_features=num_classes, bias=False)
 
    def forward(self, x):
        # Apply the backbone network to the input tensor
        backbone_output = self.backbone(x)
        # Flatten and apply the linear layer
        logits = torch.flatten(backbone_output, 1)  # Reshape the output of the backbone network to a 1D tensor (flattened tensor)
        final_logits = self.classification(logits)
        
        return final_logits

# Initializing the model with the specified number of classes
m = Model()


# Inputs to the model
input_tensor = torch.randn(2, 3, 640, 512).cuda().requires_grad_(True)
output1 = m(input_tensor)

input_tensor = torch.randn(2, 3, 579, 512).cuda() # Input tensors should have different dimensions (the previous input tensor had size [640 x 512])
output2 = m(input_tensor)


# Inputs to the model