input_data = torch.randn(1, 3, 224, 224)
url = 'https://download.pytorch.org/models/resnet18-5c106cde.pth'
model = torch.utils.model_zoo.load_url(url)