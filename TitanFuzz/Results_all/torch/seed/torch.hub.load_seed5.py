x = torch.rand(2, 3)
model = torch.hub.load('pytorch/vision:v0.6.0', 'squeezenet1_0', pretrained=True)