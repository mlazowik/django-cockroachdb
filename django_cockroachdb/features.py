from django.db.backends.postgresql.features import (
    DatabaseFeatures as PostgresDatabaseFeatures,
)


class DatabaseFeatures(PostgresDatabaseFeatures):
    """
    Not currently supported: https://github.com/cockroachdb/cockroach/issues/18656
    """
    has_select_for_update = False
    has_select_for_update_nowait = False
    has_select_for_update_of = False
    has_select_for_update_skip_locked = False

    """
    Not currently supported: https://github.com/cockroachdb/cockroach/issues/31632
    """
    can_defer_constraint_checks = False

    """
    Not currently supported: https://github.com/cockroachdb/cockroach/issues/9683
    """
    supports_partial_indexes = False

    """
    Not currently supported: https://github.com/cockroachdb/cockroach/issues/10735
    """
    uses_savepoints = False
    can_release_savepoints = False

    # cockroachdb does support transactions, however, a bug in Django
    # (https://code.djangoproject.com/ticket/28263) breaks TestCase if
    # transactions are enabled but not savepoints. Disabling this only affects
    # tests: transactions won't be used to speed them up.
    supports_transactions = False

    """
    There are some known limitations on having DDL statements in a transaction:
        https://www.cockroachlabs.com/docs/stable/known-limitations.html#schema-changes-within-transactions
    """
    can_rollback_ddl = False

    """
    Currently not supported: https://github.com/cockroachdb/cockroach/issues/17511
    """
    supports_callproc_kwargs = False
    create_test_procedure_without_params_sql = None
    create_test_procedure_with_int_param_sql = None

    """
    Currently not supported: https://github.com/cockroachdb/cockroach/issues/10735
    """
    atomic_transactions = False

    # Not implemented by cockroachdb: https://github.com/cockroachdb/cockroach/issues/20956
    supports_sequence_reset = False

    # Unlike PostgreSQL, cockroachdb doesn't support any EXPLAIN formats
    # ('JSON', 'TEXT', 'XML', and 'YAML').
    supported_explain_formats = set()

    # Not implemented by cockroachdb: https://github.com/cockroachdb/cockroach/issues/41645
    supports_regex_backreferencing = False

    # Introspection may work but 'CREATE MATERIALIZED VIEW' (required for the
    # test) isn't implemented: https://github.com/cockroachdb/cockroach/issues/41649
    can_introspect_materialized_views = False

    introspected_big_auto_field_type = 'BigIntegerField'

    # Column ordering is supported but cockroachdb doesn't report column
    # ordering: https://github.com/cockroachdb/cockroach/issues/42175
    supports_index_column_ordering = False