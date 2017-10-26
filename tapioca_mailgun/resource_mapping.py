# coding: utf-8

RESOURCE_MAPPING = {
    'send_message': {
        'resource': '{domain}/messages',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-sending.html'
    },
    'send_mime_message': {
        'resource': '{domain}/messages.mime',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-sending.html'
    },
    'resend_message': {
        'resource': '{domain}/messages/{storage_url}',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-sending.html'
    },
    'list_domains': {
        'resource': 'domains',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-domains.html'
    },
    'domain_info': {
        'resource': 'domains/{domain}',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-domains.html'
    },
    'verify_domain': {
        'resource': 'domains/{domain}/verify',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-domains.html'
    },
    'list_domain_credentials': {
        'resource': 'domains/{domain}/credentials',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-domains.html'
    },
    'domain_credential_info': {
        'resource': 'domains/{domain}/credentials/{login}',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-domains.html'
    },
    'domain_connection_settings': {
        'resource': 'domains/{domain}/connection',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-domains.html'
    },
    'domain_tracking_settings': {
        'resource': 'domains/{domain}/tracking',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-domains.html'
    },
    'domain_open_tracking_settings': {
        'resource': 'domains/{domain}/tracking/open',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-domains.html'
    },
    'domain_click_tracking_settings': {
        'resource': 'domains/{domain}/tracking/click',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-domains.html'
    },
    'domain_unsubscribe_tracking_settings': {
        'resource': 'domains/{domain}/tracking/unsubscribe',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-domains.html'
    },
    'list_account_ips': {
        'resource': 'ips',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-ips.html'
    },
    'account_ip_info': {
        'resource': 'ips/{ip}',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-ips.html'
    },
    'list_domain_ips': {
        'resource': 'domains/{domain}/ips',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-ips.html'
    },
    'domain_ip_info': {
        'resource': 'domains/{domain}/ips/{ip}',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-ips.html'
    },
    'list_domain_events': {
        'resource': '{domain}/events',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-events.html'
    },
    'domain_total_stats': {
        'resource': '{domain}/stats/total',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-stats.html'
    },
    'list_domain_stats': {
        'resource': '{domain}/stats',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-stats.html'
    },
    'list_domain_tags': {
        'resource': '{domain}/tags',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-tags.html'
    },
    'domain_tag_info': {
        'resource': '{domain}/tags/{tag}',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-tags.html'
    },
    'list_domain_bounces': {
        'resource': '{domain}/bounces',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-suppressions.html'
    },
    'domain_bounce_info': {
        'resource': '{domain}/bounces/{address}',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-suppressions.html'
    },
    'list_routes': {
        'resource': 'routes',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-routes.html'
    },
    'route_info': {
        'resource': 'routes/{route}',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-routes.html'
    },
    'list_domain_webhooks': {
        'resource': 'domains/{domain}/webhooks',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-webhooks.html'
    },
    'domain_webhook_info': {
        'resource': 'domains/{domain}/webhooks/{webhook_name}',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-webhooks.html'
    },
    'list_account_mailing_lists': {
        'resource': 'lists/pages',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-mailinglists.html'
    },
    'add_mailing_list': {
        'resource': 'lists',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-mailinglists.html'
    },
    'mailing_list_info': {
        'resource': 'lists/{address}',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-mailinglists.html'
    },
    'mailing_list_members': {
        'resource': 'lists/{address}/members/pages',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-mailinglists.html'
    },
    'mailing_list_member': {
        'resource': 'lists/{address}/members/{member_address}',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-mailinglists.html'
    },
    'add_member_to_mailing_list': {
        'resource': 'list/{address}/members',
        'docs': 'http://mailgun-documentation.readthedocs.io/en/latest/api-mailinglists.html'
    },
    'validate_email_address': {
        'resource': 'address/validate',
        'docs': 'https://documentation.mailgun.com/en/latest/api-email-validation.html'
    },
    'parse_email_addresses': {
        'resource': 'address/parse',
        'docs': 'https://documentation.mailgun.com/en/latest/api-email-validation.html'
    },
    'private_validate_email_address': {
        'resource': 'address/private/validate',
        'docs': 'https://documentation.mailgun.com/en/latest/api-email-validation.html'
    },
    'private_parse_email_addresses': {
        'resource': 'address/private/parse',
        'docs': 'https://documentation.mailgun.com/en/latest/api-email-validation.html'
    },
}
