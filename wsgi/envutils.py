import os

def set_local_or_prod(env_key, remote_path, local_path):
	if env_key in os.environ:
		return os.path.abspath(os.path.join(os.environ[env_key], remote_path))
	else:
		return os.path.abspath(local_path)
