from django.apps import AppConfig


def DEFAULT_CONFIG():
    from insuree.apps import InsureeConfig
    return {
        'can_update_deceased': InsureeConfig.gql_mutation_update_insurees_perms,
        'can_create_deceased': InsureeConfig.gql_mutation_create_insurees_perms,
        'can_delete_deceased': InsureeConfig.gql_mutation_delete_insurees_perms
    }


class InsureeDeceasedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'insuree_deceased'

    can_update_deceased = []
    can_create_deceased = []
    can_delete_deceased = []

    def ready(self):
        from core.models import ModuleConfiguration
        cfg = ModuleConfiguration.get_or_default(self.name, DEFAULT_CONFIG())
        self._configure_perms(cfg)

    def _configure_perms(self, cfg):
        self.can_delete_deceased = cfg['can_delete_deceased']
        self.can_update_deceased = cfg['can_update_deceased']
        self.can_create_deceased = cfg['can_create_deceased']
