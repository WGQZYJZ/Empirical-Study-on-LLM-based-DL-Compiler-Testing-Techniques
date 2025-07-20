x = torch.randn(1, 3, 224, 224)
model = torch.hub.load_state_dict_from_url('https://download.pytorch.org/models/resnet50-19c8e357.pth', progress=True)