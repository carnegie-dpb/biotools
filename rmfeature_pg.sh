#!/bin/sh
#
# Remove a particular feature from a PostgreSQL GBrowse annotation database. Assumes command-line auth for localhost db (no username, password supplied).
#
# input: db name, feature tag (e.g. mRNA:ensembl)

if [[ $# -eq 0 ]] ; then
    echo "rmeature_pg.sh <db> <feature-tag>"
    exit 1
fi

if [[ $# -eq 1 ]] ; then
    echo "rmeature_pg.sh <db> <feature-tag>"
    exit 1
fi

psql -c "DELETE FROM parent2child WHERE id IN (SELECT id FROM feature WHERE typeid=(SELECT id FROM typelist WHERE tag='$2'));" $1
psql -c "DELETE FROM name WHERE id IN (SELECT id FROM feature WHERE typeid=(SELECT id FROM typelist WHERE tag='$2'));" $1
psql -c "DELETE FROM attribute WHERE id IN (SELECT id FROM feature WHERE typeid=(SELECT id FROM typelist WHERE tag='$2'));" $1
psql -c "DELETE FROM feature WHERE typeid=(SELECT id FROM typelist WHERE tag='$2');" $1
psql -c "DELETE FROM typelist WHERE tag='$2';" $1


