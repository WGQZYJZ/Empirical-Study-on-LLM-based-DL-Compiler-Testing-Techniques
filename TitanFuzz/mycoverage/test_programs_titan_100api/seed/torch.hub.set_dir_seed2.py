input_data = torch.randn(5, 3)
torch.hub.set_dir('/tmp/hub_dir')
model = torch.hub.load_state_dict_from_url('https://s3.amazonaws.com/pytorch/models/resnet18-5c106cde.pth')